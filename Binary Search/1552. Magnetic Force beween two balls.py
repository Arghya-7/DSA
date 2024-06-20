class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def counter(d):
            curr = position[0]
            answer = 1
            for i in position:
                if (i - curr) >= d:
                    answer += 1
                    curr = i
            return answer
        minimum = 0
        maximum = position[len(position) - 1] - position[0]
        answer = 0
        while minimum <= maximum:
            mid = (minimum + maximum)//2
            if counter(mid) >= m:
                answer = max(answer,mid)
                minimum = mid + 1
            else:
                maximum = mid - 1
        return answer
