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
typedef long long LL;
LL __gcd(LL x, LL y){
    if(x % y == 0) return y;
    return __gcd(y,x%y);
}
void rotate(vector<int>& nums, int k) {
    // n^2 complexity
    int n = nums.size();
//    k = k%n;
    for(int c = 0; c < k; ++c) {
        int last = nums[n-1];
        for(int i = n-1; i > 0; --i) {
            nums[i] = nums[i-1];
        }
        nums[0]=last;
    }
}
void rotate2(vector<int>& nums, int k) {
     // n complexity
     int n = nums.size();
     k = k%n;
     if(k == 0) k = n;
     int g = __gcd(n,k);
     for(int i = 0; i < g; ++i)
         for(int j = 0; j <  n / g; ++j)
             swap(nums[i], nums[ ( i + j * k ) % n ] );
}
void solve() {
    // code goes here
    int n,k; cin >> n >> k;
    vector<int> v(n);
    for(int i = 0; i < n; ++i) cin >> v[i];
    rotate2(v,k);
    for(int i = 0; i < n; ++i)cout<<v[i]<<" ";
    cout<<endl;
}


int main(int argc, char const *argv[])
{
	fastio;
	t_times {
	    solve();
	}
	return 0;
}