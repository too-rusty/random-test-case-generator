#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <algorithm>
#include <cassert>
#include <climits>
using namespace std;

#define fastio ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define t_times int t; cin >> t; while(t--)
typedef long long LL;
LL __gcd(LL x, LL y){
    if(x % y == 0) return y;
    return __gcd(y,x%y);
}


void dfs(vector<string>& board, int i, int j, int n,int m) {
    if(i >= n || j >= m || i < 0 || j < 0) return;
    if(board[i][j] == 'X' || board[i][j] == '1') return;
    board[i][j] = '1';
    dfs(board,i-1,j,n,m);
    dfs(board,i,j-1,n,m);
    dfs(board,i+1,j,n,m);
    dfs(board,i,j+1,n,m);
}

void island(vector<string>& board) {
    int n = board.size();
    if(n == 0) return;
    int m = board[0].size();

    for(int i = 0; i < n; ++i)
        for(int j = 0; j < m; ++j)
            if(i == 0 || i == n-1 || j == 0 || j == m-1)
                dfs(board,i,j,n,m);

    for(int i = 0; i < n; ++i)
        for(int j = 0; j < m; ++j)
            if(board[i][j] == '1') board[i][j] = 'O';
            else board[i][j] = 'X';

}


vector<vector<int>> merge(vector<vector<int>>& intervals) {
    vector<vector<int>>vv;
    int n = intervals.size();
    if(n == 0) return vv;
    auto comp = [] (vector<int>& i1, vector<int>& i2) {
        if(i1[0] < i2[0]) return 1;
        if(i1[0] == i2[0]) return (int)(i1[1]<i2[1]);
        return 0;
    };
    auto intersect = [] (int& a,int& b,int c,int d) {
        if(c <= b) {
            b = max(b,d);
            return 1;
        }

        return 0;
    };

    sort(intervals.begin(),intervals.end(),comp);
    int nowL=intervals[0][0], nowR=intervals[0][1];
    for(int i = 0; i < n; ++i) {

        if(intersect(nowL,nowR,intervals[i][0],intervals[i][1])) {
        } else {
            vector<int>tmp({nowL,nowR});
            nowL = intervals[i][0], nowR = intervals[i][1];
            vv.push_back(tmp);
        }
    }
    vector<int>tmp({nowL,nowR});
    vv.push_back(tmp);
    return vv;
}

int findPeakElement(vector<int>& a) {
    int n = a.size();
    if(n == 0) return -1;
    for(int i = 0; i < n; ++i) {
        bool greater = 1;
        if(i>0 and a[i]<=a[i-1])greater = false;
        if(i<n-1 and a[i]<=a[i+1])greater=false;
        if(greater) return i;
    }
    return -1;
}

void solve() {
    // code goes here
    int n,m; cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; ++i)
        cin >> v[i];
//    island(v);
    cout<<findPeakElement(v)<<endl;
}
typedef pair<int,int> ii;
void solve22() {
    int n; cin >> n;
	std::vector<pair<int,int>> tim(n);
	std::vector<bool> vis(2*n+1);
	for(int i = 0; i < n; ++i) {
		cin >> tim[i].first >> tim[i].second;
		if(tim[i].first <= 2*n and tim[i].second <= 2*n) {
			vis[tim[i].first] = 1;
			vis[tim[i].second] = 1;
		}
	}
	for(int i = 1; i < 2*n + 1; ++i) {
		if(!vis[i]) {
			cout<<"Invalid\n";
			return ;
		}
	}
	// cout<<"ok\n";
	sort(tim.begin(), tim.end());
	stack<ii>stk;
	bool valid = true;
	for(ii& p : tim) {
		if(p.first >= p.second) valid = false;
		while(!stk.empty() and stk.top().second < p.first)
			stk.pop();
		if(!stk.empty() and stk.top().second <= p.second) valid = false;
		stk.push(p);
	}
	if(valid) cout<<"Valid\n";
	else cout<<"Invalid\n";
}

int main(int argc, char const *argv[])
{
	fastio;
//	t_times {
	    solve22();
//	}
	return 0;
}