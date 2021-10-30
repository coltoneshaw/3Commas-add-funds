# Summary

This is used to programmatically add a specific amount of funds to your 3Commas paper trading account. Paper trading requires a 3Commas subscription.

# Steps

1. Log into 3Commas and open your paper account
2. Click My Exchanges then the view icon on your paper trading account
3. Right click on the screen and inspect the page
4. Click the network tab
5. Click the `+$` next to your paper account name, this will add $1000 to your paper account
6. Within your network tab you should see a `POST` with the file `papertrading_deposit`. Copy those headers.

    The network call with be at the top by default, but you can use the filter and filter for `paper` and find it easier.

    Firefox
    1. Right click the network call
    2. Copy > copy request headers
    3. Paste this into a notepad
    4. Copy everything to the right of `Cookie: `
    5. Paste into the `cookie.txt` file. Make sure to **not** include `Cookie: ` into your string.

    Chrome
    1. Right click the network call
    2. Copy > Copy as cURL. Note do note use `Copy all as cRURL`.
    3. Paste this into a notepad
    4. The contents next to `-H 'cookie: ` in this file are what you need to copy. Remove the trailing `' \` from the end of the string.
    5. Paste into the cookie.txt file. Make sure to **not** include the `-H 'cookie: ` or `' \`

## 7. Run the function

    Replace the `account_id` with your paper trading account id and `total_funds` with the total amount of funds you want to add to paper

    Example: 
    ```
    python3 addfunds.py account_id total_funds
    ```

    You will see `b'{"message":"Deposit successful"}'` printed for each $1000 that is added to your account.

