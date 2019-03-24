// 递归实现1
class Solution {
    public int length = 0;
    public List<List<Integer>> result = new ArrayList<>();
    public int[] nums;
    public List<List<Integer>> subsets(int[] nums) {
        this.length = nums.length;
        this.nums = nums;
        List<Integer> temp = new ArrayList<>();
        Backtrace(0, temp);
        return this.result;
    }

    public void Backtrace(int depth, List<Integer> temp) {
        if(depth >= this.length)
            this.result.add(new ArrayList<Integer>(temp));
        else
            for(int i=0;i<2;i++) {
                List<Integer> t = new ArrayList<>(temp);
                if(i==0) {
                    Backtrace(depth+1,t);
                } else {
                    t.add(this.nums[depth]);
                    Backtrace(depth+1,t);
                }
            }
    }
}
//递归实现2
class Solution {
    public int length = 0;
    public List<List<Integer>> result = new ArrayList<List<Integer>>();
    public int[] nums;
    public List<List<Integer>> subsets(int[] nums) {
        this.length = nums.length;
        this.nums = nums;
        List<Integer> temp = new ArrayList<Integer>();
        Backtrace(0, temp);
        return this.result;
    }

    public void Backtrace(int depth, List<Integer> temp) {
        this.result.add(new ArrayList<Integer>(temp));
        for(int i=depth;i<this.length;i++) {
            temp.add(nums[i]);
            Backtrace(i+1,temp);
            temp.remove(temp.size()-1);
        }
    }
}
//非递归实现
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        result.add(new ArrayList<Integer>());
        for(int i=0;i<nums.length;i++){
            int size = result.size();
            for(int j=0;j<size;j++) {
                List<Integer> temp = new ArrayList<Integer>(result.get(j));
                temp.add(nums[i]);
                result.add(new ArrayList<Integer>(temp));
            }
        }
        return result;
    }
}