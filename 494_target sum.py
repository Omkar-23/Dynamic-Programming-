class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1  
        for num in nums:
            updated_counts = defaultdict(int)
            for key, val in counts.items():
                updated_counts[key + num] += val
                updated_counts[key - num] += val
            counts = updated_counts
        return counts[target]  
    

