class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
    let s = new Set(nums);
    return s.size < nums.length;
    }
}