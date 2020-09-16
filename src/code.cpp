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

bool containsDuplicate(vector<int>& nums) {
    set<int> S(nums.begin(), nums.end());
    return nums.size() != S.size();
}

bool containsNearbyDuplicate(vector<int>& nums, int k) {
    map<int,int> last_seen; bool res = false;
    for(int i = 0; i < nums.size(); ++i) {
        if(last_seen.count(nums[i])) {
            res |= (i-last_seen[nums[i]] <= k);
        }
        last_seen[nums[i]] = i;
    }
    return res;
}

void solve() {

    int n, m; cin >> n >> m;
    vector<int> v1(n+m);
    for(int i = 0; i < n+m; ++i) {
        cin >> v1[i];
    }
    sort(v1.begin(),v1.end());
    cout<<m+n<<endl;
    for(int i : v1) cout<< i<< " ";
    cout<<endl;
//    for(int i = 0; i < m; ++i) {
//        cin >> v2[i];
//    }

//    cout<<(containsNearbyDuplicate(v,k) ? "YES" : "NO")<<endl;;

}


void moveZeroes(vector<int>& nums) {
    int i = 0;
    int n = nums.size();
    if(n == 0) return ;
    while(i < n and nums[i] != 0) ++i;
    for(int j = 0; j < n and i < n; ++j) {
        if(i < j and nums[j] !=0 ) {
            swap(nums[i],nums[j]);
            while(i < n and nums[i] != 0) ++i;
        }
    }
}
int removeDuplicates(vector<int>& nums) {
    int n = nums.size();
    if(n == 0 || n == 1) return n;
    int idx = 0;
    // int cnt = 1;
    for(int i = 1; i < n; ++i) {
        if(nums[i] == nums[i-1]) continue;
        nums[idx++] = nums[i-1];
    }
    nums[idx++] = nums[n-1];
    return idx;
}



int majorityElement(vector<int>& nums) {
    int n = nums.size();
    map<int,int> cnt;
    for(int i = 0; i < n; ++i) {
        cnt[nums[i]]++;
    }
    for(auto i : cnt) if(i.second > n/2) return i.first;
    return -1;

}




long long titleToNumber(string s) {
    reverse(s.begin(), s.end());
    long long x = 0, p =1;
    long long n = s.length();
    for(int i = 0; i < n; ++i) {
        x+=p*(s[i]-'A'+1);
        p*=26;
    }
    return x;
}

void solve3() {
    string s; cin >> s;
    cout<<titleToNumber(s)<<endl;
}

void solve2() {
    int n; cin >> n; vector<int> v(n);
    for(int i = 0; i < n; ++i) cin >> v[i];
    int x = majorityElement(v);
    cout<<x<<endl;
//    for(int i = 0; i < x; ++i) cout<<v[i] << " ";
//    cout<<endl;
}

string convertToTitle(int n) {
    long long P = 1;
    vector<long long> arr(11);
    for(int i = 0; i < 11; ++i) { arr[i] = P; P*=26; }
    for(int till = 10; till >= 0; --till) {
        long long p = arr[till];
        bool baap = true;
        long long nn = n;
        string ans = "";
        for(int i = till; i>= 1; --i) {
            bool beta = false;
            for(int j = 26; j >= 1; --j) {
                if(p*j < nn) {
                    nn -= p*j;
                    ans += (char)(j-1 + 'A');
                    beta = true;
                    break;
                }
            }
            baap = baap & beta;
            p /= 26;
        }
        if(nn>=1 and nn<=26){
            ans += nn-1+'A';
            nn=0;
        }
        if(baap and nn == 0) return ans;
    }
    return "";
}

vector<vector<int>> threeSum(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> ans;
    if(n < 3) return ans;
    sort(nums.begin(), nums.end());
    vector<int> numss;
    map<int,int> cnt;
    cnt[nums[0]]++;
    for(int i=1; i < n; ++i) {
        cnt[nums[i]]++;
        if(nums[i]!=nums[i-1]) numss.push_back(nums[i-1]);
    }
    numss.push_back(nums[n-1]);

    n = numss.size();
    for(int j = 0; j < n; ++j) {
        for(int i = 0; i < j; ++i) {
            int s= numss[i] + numss[j];
            cnt[numss[i]]--; cnt[numss[j]]--;
            if(cnt.count(-s) and -s <= numss[i] and cnt[-s] > 0) {
                vector<int> tmp({-s,numss[i],numss[j]});
                ans.push_back(tmp);
            }
            cnt[numss[i]]++; cnt[numss[j]]++;
        }
        if(cnt[numss[j]] >=2 ) {
            cnt[numss[j]] -= 2;
            int s = 2*numss[j];
            if(cnt.count(-s) and -s <= numss[j] and cnt[-s] > 0) {
                vector<int> tmp({-s,numss[j],numss[j]});
                ans.push_back(tmp);
            }
            cnt[numss[j]] += 2;
        }
    }
    if((int)ans.size() > 0) sort(ans.begin() , ans.end());
    return ans;
}


int threeSumClosest(vector<int>& nums, int target) {
    set<int> s;
    sort(nums.begin(), nums.end());
    s.insert(nums[0] + nums[1]);
    int n = nums.size();
    int dis = INT_MAX, val = -1;
    for(int j = 2; j < n; ++j) {

        int x = target-nums[j];

        auto z = s.lower_bound(x);
        if(z!=s.end() and abs(target-nums[j]-*z) < dis) {
            dis = abs(target-nums[j]-*z);
            val = nums[j] + *z;
        }
        if(z!=s.begin()) --z;
        if(abs(target-nums[j]-*z) < dis) {
            dis = abs(target-nums[j]-*z);
            val = nums[j] + *z;
        }

        for(int i = 0; i < j; ++i) s.insert(nums[i]+nums[j]);

    }
    return val;
}

void solve4() {
    long long n, k; cin >> n >> k;
    vector<int> v(n);
    for(int i = 0; i < n; ++i) cin >> v[i];
    cout<<threeSumClosest(v,k)<<endl;;
//    auto z = threeSum(v);
//    cout<<(int)z.size()<<endl;
//    for(auto& i : z) {
//        for(int k : i) cout<<k<<" ";
//        cout<<endl;
//    }
}



int threeSumSmaller(vector<int>& nums, int target) {
    if((int)nums.size() == 0) return 0;
    int n = nums.size();
    sort(nums.begin(), nums.end());
    int ans = 0;
    for(int i = 0; i < n; ++i) {
        for(int j = i + 1; j < n; ++j) {
            int x = nums[i] + nums[j];
            int idx = lower_bound(nums.begin(),nums.end(),target-x) - nums.begin();
            --idx;
            if(idx > j) ans += idx - j;
        }
    }
    return ans;
}

int subarraySum(vector<int>& nums, int k) {
    map<int,int> m;
    m[0] = 1;
    int s = 0, ans=0;;
    for(int i : nums) {
        s += i;
        ans += m[s-k];
        m[s] += 1;
    }
    return ans;
}

void solve5() {
    int n, k; cin >> n >> k;
    vector<int> nums(n);
    for(int i = 0; i < n; ++i) cin >> nums[i];
    cout<<subarraySum(nums, k)<<endl;;
}



int minCostClimbingStairs(vector<int>& cost) {
    int n = cost.size();
    if(n == 0) return 0;
    vector<int> dp(n+1);
    // dp[0] = 0;
    // dp[1] = 1];
    for(int i = 2; i <= n; ++i) {
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]);
    }
    return dp[n];
}

vector<int> majorityElement2(vector<int>& nums) {
    vector<int> ans;
    map<int,int> cnt;
    int n = nums.size();
    for(int i : nums) {
        cnt[i] ++;

    }
    for(auto i : cnt) if(i.second > n / 3) ans.push_back(i.first);
    return ans;
}

void solve6() {
    int n; cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; ++i) cin >> nums[i];
    vector<int> ans = majorityElement2(nums);
    cout<<ans.size()<<endl;
    sort(ans.begin(),ans.end());
    for(int i: ans) cout<<i<<" ";
    cout<<endl;
}


bool isSubsequence(string s, string t) {
    int j = 0;
    for(int i = 0; i < t.length(); ++i) {
        if(t[i] == s[j]) ++j;
    }
    return j == s.length();
}

void solve7() {
    string s1, s2;
    cin >> s1 >> s2;
    cout<<(isSubsequence(s1,s2) ? "YES" : "NO") << endl;
}

void solve8() {
    int n; cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; ++i) cin >> a[i];
    cout<<*max_element(a.begin(), a.end())<<endl;

}

int main(int argc, char const *argv[])
{
	fastio;
	t_times {
	    solve8();
	}
	return 0;
}