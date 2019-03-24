class Solution {
    public List<Integer> partitionLabels(String S) {
        HashMap<Character, Integer> last = new HashMap<Character, Integer>();
        List<Integer> result = new ArrayList<Integer>();
        result.add(-1);
        for(int i=0;i<S.length();i++) {
            last.put(S.charAt(i),i);
        }
        int flag = last.get(S.charAt(0));
        for(int i=0;i<S.length();i++) {
            if(i<flag) {
                if(last.get(S.charAt(i)) > flag)
                    flag = last.get(S.charAt(i));
            }
            if(i == flag) {
                result.add(flag);
                result.set(result.size()-2, result.get(result.size()-1)-result.get(result.size()-2));
                if(flag+1<S.length())
                    flag = last.get(S.charAt(flag+1));
            }
        }
        result.remove(result.size()-1);
        return result;
    }
}