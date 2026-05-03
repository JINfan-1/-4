import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        print("错误：未设置 DEEPSEEK_API_KEY")
        sys.exit(1)
    return api_key

def main():
    api_key = get_api_key()
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )

    print("=== DeepSeek 终端对话程序 ===")
    print("输入 exit / quit / q 退出\n")

    while True:
        user_input = input("你: ").strip()
        
        # 退出指令
        if user_input.lower() in {"exit", "quit", "q"}:
            print("程序已退出")
            break
        
        # 空输入跳过
        if not user_input:
            continue

        # AI 回复
        print("DeepSeek: ", end="")
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": user_input}],
                stream=True
            )
            for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    print(content, end="")
            print("\n")
        except Exception as e:
            print(f"\n出错：{e}\n")

if __name__ == "__main__":
    main()