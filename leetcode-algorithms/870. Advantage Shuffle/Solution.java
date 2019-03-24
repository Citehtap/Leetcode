// 方法1
// 将A进行排序，遍历B，找到比B[i]大的最小的值
class Solution {
    public int[] advantageCount(int[] A, int[] B) {
        Arrays.sort(A);
        List<Integer> list = new ArrayList<>();
        for(int i = 0 ; i < A.length ; i++){
            list.add(A[i]);
        }
        int [] C = new int [A.length];
        for(int i =0 ; i < C.length ; i++){
            C[i] = Integer.MIN_VALUE;
            for(int j = 0; j < list.size() ; j++ ){
                if(list.get(j) > B[i]){
                    C[i] = list.remove(j);
                    break;
                }
            }
        }
        for(int i = 0 ; i < C.length; i++){

           if(C[i] == Integer.MIN_VALUE){
                C[i] = list.remove(0);
            }
        }
        return C;
    }
}