pragma solidity ^0.6.0;

import "../interfaces/OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/token/ERC20/ERC20.sol";
import "../interfaces/OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/token/ERC20/SafeERC20.sol";
import "../interfaces/OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/access/Ownable.sol";
import "./GasToken.sol";

contract Transfer is Ownable {
    using SafeERC20 for ERC20;
    address constant ETHER = address(0);

    receive() external payable {}

    function transfer(
        address _assetAddress,
        address payable _transferTo,
        uint256 _transferAmount
    ) public onlyOwner {
        if (_assetAddress == ETHER) {
            _transferTo.transfer(_transferAmount);
        } else {
            ERC20(_assetAddress).safeTransfer(_transferTo, _transferAmount);
        }
    }

    function transferWithGasToken(
        address _assetAddress,
        address payable _transferTo,
        uint256 _transferAmount,
        address _gasToken,
        uint256 _gasTokenAmount
    ) public onlyOwner {
        if (_assetAddress == ETHER) {
            _transferTo.transfer(_transferAmount);
        } else {
            ERC20(_assetAddress).safeTransfer(_transferTo, _transferAmount);
        }
        require(GasToken(_gasToken).freeFrom(msg.sender, _gasTokenAmount));
    }

    function transferAndDestruct(
        address _assetAddress,
        address payable _transferTo,
        uint256 _transferAmount
    ) public onlyOwner {
        if (_assetAddress == ETHER) {
            _transferTo.transfer(_transferAmount);
        } else {
            ERC20(_assetAddress).safeTransfer(_transferTo, _transferAmount);
        }
        selfdestruct(msg.sender); // transfer remaining eth balance to the owner contract
    }
}
