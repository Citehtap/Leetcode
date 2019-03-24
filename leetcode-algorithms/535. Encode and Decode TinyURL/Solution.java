public class Codec {
    Map<Integer,String> map1 = new HashMap<Integer,String>();
    Map<String,Integer> map2 = new HashMap<String,Integer>();
    String s = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public String encode(String longUrl) {
        if(!map1.containsKey(longUrl)) {
            map1.put(map1.size()+1, longUrl);
            map2.put(longUrl, map2.size()+1);
        }
        int n = map2.get(longUrl);
        StringBuilder sb=new StringBuilder();
        while(n>0) {
            int r = n%62;
            n /= 62;
            sb.insert(0,s.charAt(r));
        }
        return sb.toString();
    }

    public String decode(String shortUrl) {
        int val = 0;
        int length = shortUrl.length();
        for(int i=0;i<length;i++) {
            val = val*62+s.indexOf(shortUrl.charAt(i));
        }
        return map1.get(val);
    }
}