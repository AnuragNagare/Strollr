import scrapy

class KidsActivitySpider(scrapy.Spider):
    name = 'kids_activity'
    start_urls = ['https://www.timeout.com/kids']  # Time Out Kids website URL

    def parse(self, response):
        # Extract activity listings from the site
        activities = response.css('div.listing')  # Modify this selector based on actual site structure
        for activity in activities:
            # Extract event details
            event_name = activity.css('h3.card-title::text').get()
            description = activity.css('p.card-description::text').get()
            date = activity.css('span.card-meta-time::text').get()
            location = activity.css('div.card-meta-location span::text').get()
            age_group = self.extract_age_group(activity)

            yield {
                'event_name': event_name.strip() if event_name else '',
                'description': description.strip() if description else '',
                'date': date.strip() if date else '',
                'location': location.strip() if location else '',
                'age_group': age_group.strip() if age_group else '',
            }

    def extract_age_group(self, activity):
        """Extract or assign default age group if not present"""
        # You may need to modify this based on how the age group is listed on the page
        age_group = activity.css('span.age-group::text').get()
        return age_group if age_group else 'All ages'  # Default to 'All ages' if not found
