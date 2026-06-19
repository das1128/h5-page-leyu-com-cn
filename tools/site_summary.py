import json
from datetime import datetime

# 内置站点资料
SITE_DATA = [
    {
        "name": "乐鱼体育",
        "url": "https://h5-page-leyu.com.cn",
        "tags": ["体育", "娱乐", "电竞", "真人"],
        "description": "综合性体育娱乐平台，涵盖体育赛事、电子竞技、真人娱乐等多种互动内容。",
        "keywords": ["乐鱼体育", "体育娱乐", "电竞平台", "真人娱乐"]
    }
]

def build_summary(item):
    """为单个站点构建结构化摘要"""
    return {
        "site_name": item["name"],
        "url": item["url"],
        "tags": ", ".join(item["tags"]),
        "keywords": ", ".join(item["keywords"]),
        "description": item["description"],
        "summary_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def format_summary(summary_dict):
    """格式化摘要为可读文本"""
    lines = []
    lines.append("=" * 40)
    lines.append(f"站点名称：{summary_dict['site_name']}")
    lines.append(f"站点URL：{summary_dict['url']}")
    lines.append(f"标签：{summary_dict['tags']}")
    lines.append(f"关键词：{summary_dict['keywords']}")
    lines.append(f"简介：{summary_dict['description']}")
    lines.append(f"摘要时间：{summary_dict['summary_time']}")
    lines.append("=" * 40)
    return "\n".join(lines)

def generate_json_output(summaries):
    """将摘要列表输出为JSON字符串"""
    return json.dumps(summaries, ensure_ascii=False, indent=2)

def show_all_summaries(data):
    """展示所有站点的摘要信息"""
    summaries = []
    for item in data:
        summary = build_summary(item)
        summaries.append(summary)
        print(format_summary(summary))
        print()
    return summaries

def export_summaries_to_file(data, filename="site_summary_output.json"):
    """将摘要导出到JSON文件"""
    summaries = []
    for item in data:
        summaries.append(build_summary(item))
    json_content = generate_json_output(summaries)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_content)
        print(f"摘要已导出至：{filename}")
    except IOError as e:
        print(f"写入文件失败：{e}")

def main():
    print("【内置站点资料摘要生成器】")
    print(f"共加载 {len(SITE_DATA)} 个站点资料\n")
    
    summaries = show_all_summaries(SITE_DATA)
    
    # 额外展示JSON格式
    print("JSON格式摘要：")
    print(generate_json_output(summaries))
    
    # 导出到文件
    export_summaries_to_file(SITE_DATA)

if __name__ == "__main__":
    main()