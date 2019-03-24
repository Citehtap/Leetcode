"""
用一个指针re指向可能需要原地修改的位置。遍历数组nums：
    re<2时，不需要修改；
    re>2时，若某个数已超过2个，则re会停留在第三个数字上，当遍历到其他不同数字时进行修改。
"""
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int re = 0;
        for(int i=0;i<nums.size();i++) {
            if(re<2 || nums[i]!=nums[re-2]) {
                nums[re] = nums[i];
                re++;
            }
        }
        return re;
    }
};