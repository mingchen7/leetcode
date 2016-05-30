'''
Created on Oct 16, 2015

@author: mingchen7
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dict = {}
        leng = len(s)
        for i in range(leng-9): 
            str = s[i:i+10]
            if str not in dict.keys():
                dict[str] = 1
            else:
                dict[str] += 1
        
        result = []
        for s in dict:
            if dict[s] > 1:
                result.append(s)
        
        return result
    
s = Solution()
str = "CCTATTTAAGGGAATCGCGGTCAACTATGTTGCCAGAATATAGGATGGAAAGCAGACTCGCCGGCAGACGCTCTGAGATTCTCTGTAATCGATCTGAGTTCATAAGCGACTCATAGACACCGTAGGCCATGACGGGGGAGGTGCGGGTAGTCGCAAAAAAAATGTGGCCTGCGTTCCGAAAGTTAATCGTAAGGACCTCTTAAGGTCAATTTCCGTAGTGATATAACGGACGCGACTTTAGGATACTATATTGCCCCACATTAACTCCCTTCCCTCTGCAATCGGCATGTGCTCCCGAGGTATACTGTCTTCGGAACAAACTGAATCCATACACCTCTTATCGACCCAGCACCTCCGAAAAGGAAATCGACGCCCCAACATTATACGCCTAGACAATTGCAACATAGAGCGAGACGTAGCGATCCAAACGAGCTAACAGCTCGAGATAACGAGTGCCTACGGCGATCGATGTCAAACGTCCAAGTGCATACTCGCTAGGACATTGGCTCATCAGGACTCAACTTAGTAGCTGATGCTGCTAGTTTAACGTCTTGTAATCAATATAGAGCATTGCACGGACACCAGCGCTCAACCTGGAGATGCCTTGTCTCGGAAAAACTGCATTCTGTAATAACCACGGGGTGCCACATTCCGGAACCGGGATCCGTCAAGCATGCCTTTCCGATTCATCGCGGGGTACCTCTGGCTTCCTTGAACCTGGGTGGGTATAAAATAACCGGTTTTAAGTGGCTCGACAGAGCGGGAAGCAGGCGCTATCATCAGGTTTTTACGGATTTATAGAGACCTCTTGTGCAGCAATACCTCTTTAATCCAATGTGGGCGCCCCCTTCATAGGGTCACGTCAGCATGATTCGTCGGGCCGAGGGACATGACTGACGACCGTTGGCAATACCCCGACCTCTAAAATTGTCCAACAGTGTGGTAGGTTATCCTGGTGACGCGGTATGACGGTCGATGCGAGCGTGTAGAAAGATGACGAGAGAGTCATCTCACAACATTGCGTGCTGTTTGGATCATACACCCCTGTGGAGGGCTTACCAGAAAGTGGACGCAGAAAGCCACCAAAAGTGTCATGCCAGATACCTGGCCTCCTTCGCCGCCGCGACTGAAGACCTTCCTTTAATTCCGTTATCCTACTTACGACCGAGAGTCAGATCTGTCAGTAAAGATCGGTCTGTTGCTTTCCACGGACTGTGAAGAATCCGCTGTTCTAACCAGCCAGCCCATTATACGGATCGATTTTGAAGTAACCTAGTAGGCGAATCAGCGGCCGGGCCTGATGCTAGACTCCCTAGACAATTTCCTCTCCACGGAAGGTTCCTAATCCCTGGGAATTTGGCTTATACGGGCCTTGGACACTGTTAAACTTCAGAGTGATAATTTAATGGCGAAGCTCTACGCCAGCGACCGCCGAAGCTCGCACCTTTAGCCCCCCTGAGTGAAGAACACTCGGGAATCTGCTCTCCTTGCAACCAAGCAACGGCGGGGTAGATATGGTGGGTTTCATGACGGCCCGGGAAGCTCTGGTCATAGCAATACTTGGGTAGCTGTGATGAGGGTCCAAAACTTTTTGGGCCAAGGTTCGGACGACACCGTCCGATCGACTGCCTAACTACCTGTTCACCCCATCGATAGAGTACAGTCGAGGCCCCGCCCGACCCATACGTCAAGACAGTGACAATAGGTGCTTACGAGTTTCTATAATAAATTGTCGGGACGATGTCTGCCCGCCTACCTGAGTGCGTGCCCGATATGGGGCTTGCGGAAAACTATGAAATATTAGTATTGCCCGGGGGACTCAGTCGAGTATTTGTGGAGACTCCCATTGCACTACTACAGCACCATATTAAGCTTACTCAGATACGTTAGAACAATAGGGGATCCACTTAAAACATTACAGATCCCAATCGGTCTCCTTGTTAAGGAAAAGCGTTAACAGGTGTGGTGGCAGTTATATTTGTAATAGACTTATAATAGGGTATTCCAAGTTTATTGTGGATAACGTCTCAAACCTGTTCCACACCACGAGTGTGGGCAATGAGATCCTATTGGCACGTCGTTATAGTCTCAGTGCCTGAAGACACCTGAAAGCAGGCGCTGTGACGTGTACCCAGTGCCCTCTGCAACCGGGAACTAGGGTTACAGAGGGGAAACAAAAATGATCGCACGCTTTAATCCAATACCGTTTCCCGTCTCCCAAGGTGAGACACTCCGGGGTATAAGTCCAGCCTCTTGTACGGTCACGATTAGGCGAAAATCTACTGTCTACCTTCGGTGTGCATTGTCTTAGCGTCTTATCCAGAGAGGAATGGCTTTCGTCGTCGTCGCTAGTTTCGCTCGCTTGAGGTATAGTTAATAGCAAGACTACGAGTCCACTGCTTCATGTCTAATTCATCGGCAGCCCTGTTTGGATTGGAGCGTAGCTAGGACCCCCGAACCAGCCTTAACTATGAACGTTTGTCTTCAAATCTGGGCGCACGTACTTCGTAGGCTGGATATGCAGAATCTCGCCGTCGTGACGACGATCCGTTGTAGACGGCACAGCGTCTCTGACCGGCTTGAACTAATGCTGACAATTCTGACATAAGGTCTACGCATCCAGAAAGTGTAATGCATGTATGTATGCAGCCAAACGATAGTAGAGCCCTATCTCGCTTGAGAGGCACTTCCCTGTATGCAAATACCGATGTTTCTCCGCTTCATGTACTAAAACCCTGTGACCGACTAGTTGCACCTACGATTGTATGACACGACGGCCTTAGAGGCAGCAACGCGTGGTAGGCCGTTATGCGAGGAATTCTACTACAGTCGGGAGCCGCAGCGGAAGCAATTTTTTTACTCACGTTCCAGCATGCTGCAAACGGAAGCTGACACGGAGTCAATCGGGTAAATTTTGAGCAAATAAATCGCGACAACTAGTCCCGACTACGCTTTCGACACTGTCCGGCAGATTCCGTGCATCAATTAAACGTCATCAATCAATTACTGGCACGACTGTAGACGGGTGTACTCTTTTATAGACTCAGCAGTAGGACCTATGTGGAGCGGTCTACACATTGACGCAAGACACAAGAACTAGCGCGGATTGTTTGATTCGGTGACCTCTGAGGGTCGCTAAGCGACACCACAATGCGTTAGTGCTAACGTAAGAGAGCTCGATTGCTATATAGATGTCGGTATTCTTCAATGCATTTGCTTACTAGCAGCGTCGGATACTCTTGGCCGGGACCTTCTTATTAGTCAATTACAGAAACAGTTGAAAGCCCCACCAGTTGCATATACTACTGCCTCCATTGTTGATGACCTCAACTTGCCTACCAGGATTGGAGCACCGATGTTATTTCCTCCGAGGTATAACCGAGCGTCATAACTTGGATGTATCCAGACTCGCTTATCCCCTCGCTGAGCATATCCTAGTCTGGATGACTTCAGAGAGCCTTTCTGGTCCGTAATATCCCAGTAGACTGGAGTTGTAGCAAATCGACCCTTGGGTGACTGCCTCACCCTGAAGTGATGTCTCTTCTTTACCATGCAGGCACTGGTCTAGCCGCCGAGTATCTTCTGATCCTTCTAAGGGCTTATTCGAAACAGCTTAACAAATGACAGGCTGTGATGATATATTACGTTGACGCTACGGGGACAGCGCCTATGTCGGCCACTAGGGCTTCATCCGTTACTCAGGGTCAAATGGGGATTTCATATTGCGGGATCGATTGAAGATAGCATCACACGTCTCCCAAGATACGTCCCACTTTGGTTTTGGTCACTCCTTATTCCGCGACGGTAGTCCCGCGCTGTTGCAAACTCGTTTGAAGACGCCTAGTCAAGATTCACTTCGCGGATCCGGCATCTTCGAATGGTTGGGATCCAGACGAGCGTGGGCGTACTGCTTACGAGAACGACTCGGCAGTGTTAGAGTGTTATCTGAAGGAGATGCTAGTAACATAATATACAAATCTTTATGTTAGTAGACTGCACAAGTCAATATGGATACATAGGTCCATGGAAGAATGTTCACGCGTTACTTGTGTCTCGCCACGCGAGTGCATCTCCATAGAGCCTTCCTGTATCGTCACTTTCTCTCGATGGTCAGCGTTTCAATAATTCGCGAGCAACAACGTCGATCTCCGGGATATACGATCAGCCCAGAGTACAAGACCCGATATGCACGGCATGCAATATCCAGAGTCGGGCATACTTTATTGGACTGGTAAGTCTCTCCTGTCCACGCTGACTACAACTGAAGTAGTGTGACCTGACTGGCGCCTTCTACCACCCATGTCTCCAGCAATTGTCGCATCATACAGGTTCCCAGCGTAGCGTCGCCCCTTTGGCGCTTTCCTGCGGTATCGATATAATGAAATTTTCACCAACGTTGCGCTTATTCGCAAGGTGGCGAGATTGTATTATGCCACACAGCCTCCTAGAATATCCTAAGGCAGAGTTCGGTGACTTTTGCCGCTTTAGGCAGGACAGAGCTGTCCTTATCTTGGGACAGCACGTGCTTCGATATACTGCCCGCGCTTTCTCTGGGGACGCTTTAAGGTCTTTTTGCTGCGATTGCGCTATCCGAGCCACTGTATCTTATACCGACGTATCTCGGCCTCGTTACATAGAAAATACTGTCAGCGCTTGTAGCGAGACCACGCGATAGTGACCGGAGTTGGTTCCTCCGTCCTTTTTGTATTCCCCGTTGCGACTGATTCACGTGACCACATAGTCATAAGACACTGAAACAAAGCTTACTTTGGCGAGTAGGATGTGTTAATAACTTCTGGCAGCACATAGAATTGGTCCGTGGTCCTCCTTTGCGGCCACTACTGAACGTACCAATGAGTACGTATTGACCTCTTACTGAGTGTAGTAAGGGAGCATCAATCGGTCTCCGGGTTTTTGATTCATGAGTCATGCATCAGTGGTTCATCCCTTGCGTGTTATTCTCTTGATACGGTTGACTAAGCAATGAGTTAGTCGAGCTA"
result = s.findRepeatedDnaSequences(str)
print result