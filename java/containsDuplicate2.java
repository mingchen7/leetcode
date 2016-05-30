//Given an array of integers and an integer k, 
//find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

import java.util.*;

public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        if(k < 0) return false;
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i=0; i<nums.length;i++){
            if(map.containsKey(nums[i])){
                int j = map.get(nums[i]);
                if(i-j <= k){
                    return true;
                }
            }
            map.put(nums[i],i);
        }
        return false;
    }
}