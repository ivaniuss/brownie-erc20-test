# Import necessary modules
import brownie

# Define the test case for the MyToken contract
def test_mytoken_mint(accounts, MyToken):
    # Deploy the MyToken contract
    mytoken = MyToken.deploy({"from": accounts[0]})

    # Define the minting parameters
    to = accounts[1]
    amount = 100

    # Mint tokens using the onlyOwner function
    mytoken.mint(to, amount, {"from": accounts[0]})

    # Verify that the tokens were minted successfully
    assert mytoken.balanceOf(to) == amount

    # Attempt to mint tokens from a non-owner account (should raise an exception)
    with brownie.reverts("Ownable: caller is not the owner"):
        mytoken.mint(accounts[2], amount, {"from": accounts[1]})
