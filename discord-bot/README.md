# Discord Crypto Community Bot

Professional Discord bot for crypto communities with trading signals, wallet verification, and automated moderation.

## Features

- 💰 **Real-time Price Tracking** - Live crypto prices with embeds
- 🔔 **Price Alerts** - Custom notifications for price targets
- ✅ **Wallet Verification** - NFT/token holder verification system
- 📊 **Portfolio Tracking** - Member portfolio management
- 📈 **Trading Signals** - Premium signal posting with analytics
- 🤖 **Auto-moderation** - Spam protection and role management
- 📢 **Welcome System** - Automated onboarding for new members

## Tech Stack

- Python 3.10+
- discord.py 2.0+
- CoinGecko/Binance API
- Web3.py for wallet verification

## Setup

```bash
# Install dependencies
pip install discord.py requests web3

# Configure bot
export DISCORD_TOKEN="your_bot_token"
python bot.py
```

## Commands

### Public Commands
- `!price BTC` - Get current Bitcoin price
- `!alert BTC 50000` - Set price alert
- `!verify WALLET_ADDRESS` - Verify wallet ownership
- `!portfolio` - View your portfolio
- `!stats` - Server statistics

### Premium Commands (Role-gated)
- `!signal BUY BTC 45000 50000` - Post trading signal

## Use Cases

- NFT project communities
- Trading signal groups
- DAO governance servers
- Token holder verification
- Crypto education communities

## Pricing

**Fiverr Gig:** $200-$800
- Basic bot setup: $200
- With wallet verification: $400
- Full trading signals + moderation: $800

## Why Clients Pay Premium

- **NFT Projects:** Need holder verification ($400-$600)
- **Trading Groups:** Need signal automation ($500-$800)
- **DAOs:** Need governance tools ($600-$1000)

---

**Built by:** @0xdungki | Discord bot specialist | 50+ bots deployed
