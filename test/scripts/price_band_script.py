def tick(strategy):
    if strategy.get_mid_price() >= 105:
        strategy.buy_levels = 0
    else:
        strategy.buy_levels = strategy.order_levels
    if strategy.get_mid_price() <= 95:
        strategy.sell_levels = 0
    else:
        strategy.sell_levels = strategy.order_levels