#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string replaceSpace(string s) {
        int pos = s.find(" ");//查找子串在目前字符串中的位置，找不到返回-1
        while( pos != -1 )
        {
            s = s.replace(pos, 1, "%20");//将字符串中以某个位置开始的指定长度替换为目前字符串
            pos = s.find(" ");
        }
        return s;
    }
};

int main(int argc, char const *argv[])
{
    Solution solu;
    string s = "sd as   ";
    cout << solu.replaceSpace(s);
    return 0;
}