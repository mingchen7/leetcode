import java.util.*;

public class subStringPalindrome {
	public int distinctPalindrome(String s){
		if(s == null || s.length() == 0){
			return 0;
		}

		HashSet<String> set = new HashSet<String>();
		int n = s.length();		
		boolean[][] palindrome = new boolean[n][n+1];
		int count = 0;

		for(int i = 0; i < s.length(); i++){
			for(int j = i; j <= s.length(); j++){
				palindrome[i][j] = isPalindrome(i, j, s, palindrome);
				String tmp = s.substring(i,j);
				if(palindrome[i][j] && !set.contains(tmp) && j != i ){
					set.add(tmp);
					count++;

					System.out.println(tmp);
					System.out.print(i + ",");
					System.out.print(j + "\n");
				}
			}
		}

		return count;
	}

	public boolean isPalindrome(int i, int j, String s, boolean[][] palindrome){		
		if(i == j || i == j + 1){
			return true;
		}		

		if(palindrome[i][j] == true){
			return true;
		}

		return s.charAt(i) == s.charAt(j-1) && isPalindrome(i+1, j-1, s, palindrome);
	}

	public static void main (String args[]){
		subStringPalindrome sol = new subStringPalindrome();
		String s = "abcacbbbca";
		int res = sol.distinctPalindrome(s);
		System.out.println(res);
	}
}


// O(n) version
// #include <iostream>
// #include <string>
// #include <cstdlib>
// #include <time.h>

// using namespace std;

// string s = "abcacbbbca";   // string to be analyzed
// const int N = 10;          // length of s 

// int main()
// {
//   int i, j, k,   // iterators
//       rp,        // length of 'palindrome radius'
//       R[2][N+1]; // table for storing results (2 rows for odd- and even-length palindromes 

// // print s first

//   cout << s << endl;
  
// // ...then search for palindromes

//   s = "@" + s + "#"; // insert 'guards' to iterate easily over s

//   for(j = 0; j <= 1; j++)
//   {
//     R[j][0] = rp = 0; i = 1;
//     while(i <= N)
//     {
//       while(s[i - rp - 1] == s[i + j + rp]) rp++;
//       R[j][i] = rp;
//       k = 1;
//       while((R[j][i - k] != rp - k) && (k < rp))
//       {
//         R[j][i + k] = min(R[j][i - k],rp - k);
//         k++;
//       }
//       rp = max(rp - k,0);
//       i += k;
//     }
//   }

//   s = s.substr(1,N); // remove 'guards'


// // print the results

//   for(i = 1; i <= N; i++)
//   {
//     for(j = 0; j <= 1; j++)
//       for(rp = R[j][i]; rp > 0; rp--)
//       {
//         for(k = 1; k < i - rp; k++) cout << " ";
//         cout << s.substr(i - rp - 1,2 * rp + j) << endl;
//       }
//   }
//   cout << endl;
//   return 0;
// } 