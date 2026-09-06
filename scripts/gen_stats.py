#!/usr/bin/env python3
"""프로필 스탯 카드를 SVG 로 만든다.

남의 무료 인스턴스(github-readme-stats 공용 배포 등)에 얹으면 레이트리밋에 걸려
503 이 뜬다. 여기서는 GitHub API 를 직접 읽어 SVG 를 만들어 저장소에 커밋한다.
"""
import json, os, subprocess, datetime

Q = '''{user(login:"%s"){
 contributionsCollection{
  totalRepositoriesWithContributedPullRequests
  contributionCalendar{totalContributions weeks{contributionDays{contributionCount}}}}
 pullRequests(states:MERGED){totalCount}}}'''

def gh(user):
    out = subprocess.run(["gh","api","graphql","-f","query="+Q % user],
                         capture_output=True, text=True, check=True).stdout
    u = json.loads(out)["data"]["user"]
    cal = u["contributionsCollection"]["contributionCalendar"]
    days = [d["contributionCount"] for w in cal["weeks"] for d in w["contributionDays"]]
    return {
        "contributions": cal["totalContributions"],
        "active_days": sum(1 for c in days if c > 0),
        "total_days": len(days),
        "merged_prs": u["pullRequests"]["totalCount"],
        "repos": u["contributionsCollection"]["totalRepositoriesWithContributedPullRequests"],
    }

BG, INK, MUTE = "#ffd3ff", "#111111", "#6b4a6b"
W, H, PAD = 520, 132, 18
FONT = "-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"

def card(s, updated):
    cells = [
        (f"{s['contributions']:,}", "contributions", "last 12 months"),
        (f"{s['active_days']}",     "active days",   f"of {s['total_days']}"),
        (f"{s['merged_prs']:,}",    "pull requests", "merged, all time"),
        (f"{s['repos']}",           "repositories",  "contributed to"),
    ]
    cw = (W - PAD * 2) / len(cells)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">',
        f'<rect width="{W}" height="{H}" rx="10" fill="{BG}"/>',
        f'<g font-family="{FONT}" text-anchor="middle">',
    ]
    for i, (big, label, sub) in enumerate(cells):
        x = PAD + cw * i + cw / 2
        if i:
            gx = PAD + cw * i
            parts.append(f'<line x1="{gx:.1f}" y1="34" x2="{gx:.1f}" y2="{H-30}" stroke="{INK}" stroke-opacity=".13"/>')
        parts.append(f'<text x="{x:.1f}" y="66" font-size="27" font-weight="700" fill="{INK}">{big}</text>')
        parts.append(f'<text x="{x:.1f}" y="87" font-size="11.5" fill="{INK}">{label}</text>')
        parts.append(f'<text x="{x:.1f}" y="103" font-size="10" fill="{MUTE}">{sub}</text>')
    parts.append('</g>')
    parts.append(f'<g font-family="{FONT}" font-size="10" fill="{MUTE}">')
    parts.append(f'<text x="{PAD}" y="26">GitHub activity</text>')
    parts.append(f'<text x="{W-PAD}" y="26" text-anchor="end">updated {updated}</text>')
    parts.append('</g></svg>')
    return "\n".join(parts)

if __name__ == "__main__":
    user = os.environ.get("GH_USER", "PresentJay")
    s = gh(user)
    svg = card(s, datetime.date.today().isoformat())
    open(os.environ.get("OUT", "stats.svg"), "w").write(svg)
    print(json.dumps(s, ensure_ascii=False))
