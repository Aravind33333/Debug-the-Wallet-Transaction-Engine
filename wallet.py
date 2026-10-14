
def process_transactions(initial_balance, transactions):
    balance = initial_balance
    total_deposits = 0
    total_withdrawals = 0
    processed = 0
    duplicates = 0
    seen_ids = set()

    for transaction in transactions:
        transaction_id = transaction["id"]
        transaction_type = transaction["type"]
        amount = transaction["amount"]

        if transaction_id in seen_ids:
            duplicates += 1
        seen_ids.add(transaction_id)

        if amount < 0:
            continue

        if transaction_type == "deposit":
            balance -= amount
            total_deposits += amount
            processed += 1

        elif transaction_type == "withdraw":
            if balance >= amount:
                balance -= amount
                total_withdrawals += amount
                processed += 1

    return {
        "balance": round(balance, 2),
        "total_deposits": round(total_deposits, 2),
        "total_withdrawals": round(total_withdrawals, 2),
        "processed": processed,
        "duplicates": duplicates
    }
