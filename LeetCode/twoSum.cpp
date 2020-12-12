
/*
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for(int i=0; i<numbers.size()-1; i++)
        {
            for(int j=i+1; j<numbers.size(); j++)
            {
                if(numbers[i] + numbers[j] > target)
                    break;
                if(numbers[i] + numbers[j] == target)
                    return vector<int> {i+1, j+1};
            }
        };
        return vector<int> {-1, -1};
    }
    // 双指针查找
    vector<int> twoSum_1(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size()-1;
        while(i < j)
        {
            int sum = numbers[i] + numbers[j];
            if(sum < target)
                i++;
            else if(sum > target)
                j--;
            else
                return vector<int> {i+1, j+1};
        }
        return vector<int> {-1, -1};
    }
};

template <class T>
void display(T val)
{
    cout << val << " ";
}

int main(int argc, char const *argv[])
{
    vector<int> numbers = {2, 7, 11, 15};
    int target = 100;
    Solution s;
    vector<int> result = s.twoSum(numbers, target);                 //把你的程序代码插入到这里面
    for_each(result.begin(), result.end(), display<int>);

    clock_t start,finish;
    double totaltime;
    start=clock();

    for (int i = 0; i < 2147483640; i++)
    {
        i++;
    }

    finish=clock();
    totaltime=(double)(finish-start)/CLOCKS_PER_SEC;
    cout<<"\n此程序的运行时间为"<<totaltime<<"秒！"<<endl;

    return 0; 
}