import httpx
from typing import List, Dict
from datetime import datetime
from ..core.enums import BenchWeightClass, AgeCategory

class OpenPowerliftingAPI:
    """Handles all OpenPowerlifting API interactions for bench press data"""
    
    BASE_URL = "https://openpowerlifting.org/api/v1"  # Check if this is correct
    
    def __init__(self):
        self.client = httpx.AsyncClient()
    
    async def get_top_bench_lifts(
        self,
        weight_class: BenchWeightClass,
        age_category: AgeCategory,
        sex: str,
        limit: int = 25
    ) -> List[Dict]:
        """
        Get all-time top bench press results for a specific class
        """
        params = {
            'lift': 'bench',
            'weightClass': weight_class.value,
            'ageCategory': age_category.value,
            'sex': sex,
            'limit': limit,
            'sort': 'desc'
        }
        
        async with self.client as client:
            response = await client.get(f"{self.BASE_URL}/rankings", params=params)
            if response.status_code != 200:
                raise Exception(f"API request failed: {response.text}")
            return response.json()

    async def get_current_year_bench(
        self,
        weight_class: BenchWeightClass,
        age_category: AgeCategory,
        sex: str,
        limit: int = 10
    ) -> List[Dict]:
        """
        Get current year's top bench press results for a specific class
        """
        current_year = datetime.now().year
        
        params = {
            'lift': 'bench',
            'weightClass': weight_class.value,
            'ageCategory': age_category.value,
            'sex': sex,
            'year': current_year,
            'limit': limit,
            'sort': 'desc'
        }
        
        async with self.client as client:
            response = await client.get(f"{self.BASE_URL}/rankings", params=params)
            if response.status_code != 200:
                raise Exception(f"API request failed: {response.text}")
            return response.json()

    async def close(self):
        """Clean up the HTTP client"""
        await self.client.aclose()