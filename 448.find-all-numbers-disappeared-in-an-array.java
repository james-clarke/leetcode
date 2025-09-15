class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        // I believe there is a better way to do this...
        int n = nums.length;
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num)+1);
            } else {
                map.put(num, 1);
            }
        }

        ArrayList<Integer> missing = new ArrayList<>();

        for (int i=1; i<=n; i++) {
            if (!map.containsKey(i)) {
                missing.add(i);
            }
        }

        return missing;
    }
}