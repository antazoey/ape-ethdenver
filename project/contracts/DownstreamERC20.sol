// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "@openzeppelin/token/ERC20/ERC20.sol";

contract DownstreamERC20 is ERC20 {

    /// An ERC20 that requires you have a separate ERC20 (known as the "upstream")

    address private owner;
    ERC20 private upstream;

    constructor(address upstream_) ERC20("Downstream Token", "DTKN") {
        owner = msg.sender;
        upstream = ERC20(upstream_);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "!authorized");
        _;
    }

    modifier hasUpstream(address to) {
        require(upstream.balanceOf(to) > 0);
        _;
    }

    function mint(address to, uint256 amount) public onlyOwner hasUpstream(to) {
        _mint(to, amount);
    }
}
