// i 指向长度为3的山峰，l,r 指向山峰左右的位置。
class Solution {
public:
    int longestMountain(vector<int>& A) {
        int res = 0;
        int len = A.size();
        for(int i=1;i<len-1;i++){
            if(A[i]>A[i-1] && A[i]>A[i+1]) {
                int temp = 3;
                if(i-1>0) {
                    for(int l=i-2;l>=0;l--){
                        if(A[l]<A[l+1])
                            temp++;
                        else
                            break;
                    }
                }
                if(i+1<len-1) {
                    for(int r=i+2;r<len;r++) {
                        if(A[r]<A[r-1])
                            temp++;
                        else
                            break;
                    }
                }
                if(temp>res)
                    res = temp;
            }
        }
        return res;
    }
};