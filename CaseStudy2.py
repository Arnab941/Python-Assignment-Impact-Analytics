# Based on our problem statement
# Time Complexity: O(n) and Space Complexity: O(n)
# Where n is the total number of days

class Unit:
    def __init__(self):
        self.missCeremonyCount = 0
        self.totalPossibleWayCount = 0
    
class AttendanceCalculator:
    def __init__(self):
        self.dp = []

    def attendanceCalculatorUtill(self, n, possibleConsecutiveBunks):
        for i in range(n+1):
            for j in range(possibleConsecutiveBunks+1):
                for k in range(2):
                    if i == 0:
                        unit = Unit()
                        if k == 0:
                            unit.missCeremonyCount = 1

                        unit.totalPossibleWayCount = 1
                        self.dp[i][j][k] = unit
                        continue

                    if j:
                        unit = Unit()
                        unit.missCeremonyCount = (
                                                    self.dp[i-1][j-1][0].missCeremonyCount + 
                                                    self.dp[i-1][possibleConsecutiveBunks][1].missCeremonyCount
                                                )
                        unit.totalPossibleWayCount = (
                                                        self.dp[i-1][j-1][0].totalPossibleWayCount + 
                                                        self.dp[i-1][possibleConsecutiveBunks][1].totalPossibleWayCount
                                                    )
                        self.dp[i][j][k] = unit

                    else:
                        self.dp[i][j][k] = self.dp[i-1][possibleConsecutiveBunks][1]

        return self.dp[n][possibleConsecutiveBunks][1]
    
n = int(input())
obj = AttendanceCalculator()
obj.dp = [[[None for i in range(2)] for j in range(4)] for k in range(n+1)]
answer = obj.attendanceCalculatorUtill(n,3)
print(str(answer.missCeremonyCount)+'/'+str(answer.totalPossibleWayCount))
