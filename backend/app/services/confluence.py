from atlassian import Confluence
from ..core.config import settings
from datetime import datetime
import logging

class ConfluenceService:
    def __init__(self):
        self.confluence = Confluence(
            url=settings.CONFLUENCE_URL,
            token=settings.CONFLUENCE_PAT  # Using PAT instead of username/password
        )

    def get_space_content(self, space_key: str):
        try:
            pages = self.confluence.get_all_pages_from_space(space_key, start=0, limit=500)
            content = []
            
            for page in pages:
                page_content = self.confluence.get_page_by_id(
                    page['id'], 
                    expand='body.storage'
                )
                content.append({
                    'id': page['id'],
                    'title': page['title'],
                    'content': page_content['body']['storage']['value'],
                    'url': f"{settings.CONFLUENCE_URL}/pages/viewpage.action?pageId={page['id']}",
                    'last_updated': datetime.strptime(
                        page_content['version']['when'], 
                        "%Y-%m-%dT%H:%M:%S.%fZ"
                    )
                })
            
            return content
        except Exception as e:
            logging.error(f"Error fetching Confluence content: {str(e)}")
            raise