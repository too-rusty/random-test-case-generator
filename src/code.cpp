#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

#define fastio ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define t_times int t; cin >> t; while(t--)

string longestCommonPrefix(vector<string>& strs) {
    if((int)strs.size() == 0) return "";
    auto min = [] (int x,int y) {
        return x < y ? x : y;
    };
    string ans = "";
    int n = INT_MAX;
    for(string& str : strs)
        n = min(n, str.length());
    for(int i = 0; i < n; ++i) {
        int flag = 1;
        char c = strs[0][i];
        for(string& str : strs) if(str[i] != c) flag = 0;
        if(flag) ans += c;
        else break;
    }
    return ans;
}

void solve() {
    // code goes here
    int n; cin >> n;
    vector<string> strs;
    for(int i = 0; i < n; ++i) {
        string s; cin >> s;
        strs.push_back(s);
    }
    cout << longestCommonPrefix(strs) << endl;

}

int main(int argc, char const *argv[])
{
	fastio;
	t_times {
	    solve();
	}
	return 0;
}