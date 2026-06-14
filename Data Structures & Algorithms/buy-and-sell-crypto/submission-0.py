class Solution:
    # Input: prices array of int
    # Output: max profit (in same units as one element of prices)
    # only need a profit number

    def maxProfit(self, prices: List[int]) -> int:
        cheapest_so_far=prices[0] # initialize always as Day 0 price
        best_profit=0 # default state is profit=0

        for price in prices:
            # cheapest price seen so far:
            if price < cheapest_so_far:
                # update cheapest_so_far
                cheapest_so_far=price
                # otherwise keep the existing cheapest

            # calculate profit, delta of current price and lowest price thus far seen
            curr_profit = price - cheapest_so_far

            if curr_profit>best_profit:
                #update best_profit:
                best_profit=curr_profit
            
        return best_profit

# Time complexity: O(n)
# Space complexity: O(1)    