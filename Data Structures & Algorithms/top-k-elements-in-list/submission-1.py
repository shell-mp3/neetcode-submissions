class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        #function sorted() takes iterable(collection you want to sort, key is the "thing" we are sorting by, in this case its count(can be length for ex), and lastly since we want it descneding we reverse = true because we want the larger counts in front.)
        sorted_nums = sorted(count, key=count.get, reverse=True)

        return(sorted_nums[:k])
        