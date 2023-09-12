methods {
    function swapStable(uint256[],uint256[],uint256) external;
    function swapShares(uint256[],uint256[],uint256) external;
}

/* Property: Find and show a path for each method */
rule reachability(method f)
{
	env e;
	calldataarg args;
	f(e,args);
	satisfy true;
}
