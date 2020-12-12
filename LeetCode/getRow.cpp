#include <iostream>
#include <vector>

class Solution{
public:
    std::vector<int> getRow(int rowIndex) {
        std::vector<int> row_0 = {1};
        std::vector<int> row_1 = {1, 1};
        if(rowIndex == 0)
            return row_0;
        if(rowIndex == 1)
            return row_1;
        std::vector<int> before = {1, 1};
        int i = 0;
        int j;
        std::vector<int> result;
        while(i < rowIndex - 1)
        {
            result = {1, 1};
            for(j=0; j<before.size()-1; j++)
            {
                result.insert(result.end()-1, before[j] + before[j+1]);
            }
            before = result;
            i += 1; 
        }
        return result;
    }
};


int main()
{
    Solution s;
    std::vector<int> result = s.getRow(33);
    int i;
    for(i=0; i<result.size(); i++)
    {
        std::cout << result[i] << std::endl;
    }
}