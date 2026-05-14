#!/usr/bin/env python3
"""
Discord Crypto Bot - Trading Signals & Community Management
Features:
- Price alerts and trading signals
- Role-based access control
- Automated moderation
- Wallet verification
"""

import discord
from discord.ext import commands, tasks
import asyncio

# Bot configuration
DISCORD_TOKEN = "YOUR_BOT_TOKEN_HERE"
GUILD_ID = 123456789  # Your server ID

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    """Bot startup"""
    print(f"✅ {bot.user} is online!")
    print(f"📊 Connected to {len(bot.guilds)} servers")
    price_alerts.start()

@bot.command(name="price")
async def price(ctx, symbol: str):
    """Get crypto price - Usage: !price BTC"""
    symbol = symbol.upper()
    
    embed = discord.Embed(
        title=f"💰 {symbol} Price",
        description=f"Current market data for {symbol}",
        color=discord.Color.green()
    )
    embed.add_field(name="Price", value="$XX,XXX.XX", inline=True)
    embed.add_field(name="24h Change", value="+X.XX%", inline=True)
    embed.add_field(name="Volume", value="$XXX.XXM", inline=True)
    embed.set_footer(text="Data from CoinGecko")
    
    await ctx.send(embed=embed)

@bot.command(name="alert")
async def alert(ctx, symbol: str, price: float):
    """Set price alert - Usage: !alert BTC 50000"""
    symbol = symbol.upper()
    
    embed = discord.Embed(
        title="🔔 Alert Set",
        description=f"You'll be notified when {symbol} reaches ${price:,.2f}",
        color=discord.Color.blue()
    )
    
    await ctx.send(embed=embed)

@bot.command(name="verify")
async def verify(ctx, wallet_address: str):
    """Verify wallet ownership - Usage: !verify YOUR_WALLET"""
    
    # In production: verify signature
    role = discord.utils.get(ctx.guild.roles, name="Verified Holder")
    
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"✅ {ctx.author.mention} verified! Welcome to the community.")
    else:
        await ctx.send("❌ Verification role not found. Contact admin.")

@bot.command(name="portfolio")
async def portfolio(ctx):
    """Display user's crypto portfolio"""
    
    embed = discord.Embed(
        title=f"📊 {ctx.author.name}'s Portfolio",
        color=discord.Color.gold()
    )
    embed.add_field(name="BTC", value="0.5 ($25,000)", inline=False)
    embed.add_field(name="ETH", value="10 ($30,000)", inline=False)
    embed.add_field(name="SOL", value="100 ($15,000)", inline=False)
    embed.add_field(name="Total Value", value="$70,000", inline=False)
    embed.set_footer(text="Use !add to update your portfolio")
    
    await ctx.send(embed=embed)

@bot.command(name="signal")
@commands.has_role("Premium")
async def signal(ctx, action: str, symbol: str, entry: float, target: float):
    """Post trading signal - Usage: !signal BUY BTC 45000 50000"""
    
    embed = discord.Embed(
        title=f"📈 TRADING SIGNAL: {action.upper()} {symbol.upper()}",
        color=discord.Color.green() if action.upper() == "BUY" else discord.Color.red()
    )
    embed.add_field(name="Entry", value=f"${entry:,.2f}", inline=True)
    embed.add_field(name="Target", value=f"${target:,.2f}", inline=True)
    embed.add_field(name="Potential", value=f"+{((target/entry - 1) * 100):.1f}%", inline=True)
    embed.set_footer(text=f"Signal by {ctx.author.name} | Not financial advice")
    
    await ctx.send(embed=embed)

@tasks.loop(minutes=5)
async def price_alerts():
    """Background task: check price alerts"""
    # In production: check user alerts and send notifications
    pass

@bot.event
async def on_member_join(member):
    """Welcome new members"""
    channel = discord.utils.get(member.guild.channels, name="welcome")
    if channel:
        embed = discord.Embed(
            title=f"Welcome {member.name}! 👋",
            description="Use !verify to get access to exclusive channels",
            color=discord.Color.blue()
        )
        await channel.send(embed=embed)

@bot.command(name="stats")
async def stats(ctx):
    """Server statistics"""
    guild = ctx.guild
    
    embed = discord.Embed(
        title=f"📊 {guild.name} Stats",
        color=discord.Color.purple()
    )
    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.add_field(name="Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="Roles", value=len(guild.roles), inline=True)
    
    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
