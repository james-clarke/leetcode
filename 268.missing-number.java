class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int total = Math.floorDiv((n * (n+1)), 2);
        return total - Arrays.stream(nums).sum();
    }
}