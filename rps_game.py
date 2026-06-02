#!/usr/bin/env python3
"""石头剪刀布 — 与电脑对战，可多轮进行"""

import random

CHOICES = ("石头", "剪刀", "布")
ALIASES = {
    "石头": "石头",
    "剪刀": "剪刀",
    "布": "布",
    "r": "石头",
    "s": "剪刀",
    "p": "布",
}

# 键战胜 值
WINS_AGAINST = {
    "石头": "剪刀",
    "剪刀": "布",
    "布": "石头",
}


def normalize(text: str) -> str | None:
    key = text.strip().lower()
    return ALIASES.get(key) or ALIASES.get(text.strip())


def judge(player: str, computer: str) -> str:
    if player == computer:
        return "平局"
    if WINS_AGAINST[player] == computer:
        return "你赢了"
    return "你输了"


def play_round() -> str | None:
    """
    进行一轮。
    返回 "win" | "draw" | "loss" 表示有效对局；
    返回 None 表示无效输入（继续）；
    抛出 SystemExit 语义用特殊值 — 改用返回 "quit"。
    """
    raw = input("请出拳（石头 / 剪刀 / 布，输入 q 退出）: ").strip()
    if raw.lower() in ("q", "quit", "退出"):
        return "quit"

    player = normalize(raw)
    if player is None:
        print("无效输入，请输入：石头、剪刀 或 布。")
        return None

    computer = random.choice(CHOICES)
    outcome = judge(player, computer)

    print(f"你出: {player}  |  电脑出: {computer}")
    print(f"本轮结果: {outcome}")

    if outcome == "你赢了":
        return "win"
    if outcome == "平局":
        return "draw"
    return "loss"


def main() -> None:
    print("=" * 44)
    print("  石头剪刀布")
    print("  输入: 石头 / 剪刀 / 布")
    print("  输入 q 或 退出 结束游戏")
    print("=" * 44)

    wins = draws = losses = 0

    while True:
        print()
        result = play_round()
        if result == "quit":
            break
        if result is None:
            continue
        if result == "win":
            wins += 1
        elif result == "draw":
            draws += 1
        else:
            losses += 1

    total = wins + draws + losses
    print()
    if total:
        print(f"战绩: 共 {total} 局 — 胜 {wins}  平 {draws}  负 {losses}")
    print("感谢游玩，再见！")


if __name__ == "__main__":
    main()
