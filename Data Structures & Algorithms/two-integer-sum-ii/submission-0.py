class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {} # stores the visited values as keys and the index as keys

        for index, value in enumerate(numbers):
            diff = target - value
            if diff in visited:
                return [visited[diff] + 1, index + 1]
            else:
                visited[value] = index
                
