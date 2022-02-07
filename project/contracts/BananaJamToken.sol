// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "@openzeppelin/token/ERC20/ERC20.sol";

contract BananaJamToken is ERC20 {

    address private owner;

    constructor() ERC20("BananaJam", "BANJAM") {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "!authorized");
        _;
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}
