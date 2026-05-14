# Solana NFT Minter & Collection Deployer

Automated NFT collection deployment tool for Solana blockchain with Candy Machine v3 integration.

## Features

- 🎨 **Bulk Metadata Generation** - Generate thousands of NFT metadata files
- 🎲 **Rarity Distribution** - Configurable trait rarity system
- 🍬 **Candy Machine v3** - Full integration with Metaplex standard
- ⚡ **Fast Deployment** - Automated upload and minting process
- 💎 **Royalty Management** - Built-in creator royalty configuration

## Tech Stack

- Python 3.10+
- Solana Web3.py
- Metaplex Sugar CLI
- JSON metadata standard

## Setup

```bash
# Install dependencies
pip install solana web3

# Install Metaplex Sugar CLI
bash <(curl -sSf https://sugar.metaplex.com/install.sh)

# Configure Solana wallet
solana-keygen new
```

## Usage

```python
from minter import SolanaNFTMinter

# Define traits
traits = {
    "Background": ["Blue", "Red", "Green"],
    "Body": ["Robot", "Alien", "Human"],
    "Eyes": ["Laser", "Normal", "3D"]
}

# Create and deploy
minter = SolanaNFTMinter("MyCollection", supply=1000)
minter.generate_metadata(traits)
minter.create_candy_machine_config()
minter.deploy_collection()
```

## Deployment Steps

1. **Generate Metadata** - Creates JSON files for all NFTs
2. **Upload Assets** - Uploads to Arweave/IPFS via Sugar
3. **Deploy Candy Machine** - Creates on-chain minting program
4. **Verify** - Validates collection integrity
5. **Mint** - Start public/whitelist minting

## Pricing

**Fiverr Gig:** $300-$1,500
- Basic 1K collection: $300
- 10K collection with rarity: $800
- Full launch + marketing: $1,500

## Real-World Use Cases

- PFP (Profile Picture) collections
- Gaming asset NFTs
- Membership/utility tokens
- Generative art projects

---

**Built by:** @0xdungki | Solana developer since 2021
