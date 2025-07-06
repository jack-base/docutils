import os

def create_directory_structure(root_dir):
    """根据指定的文件树结构创建目录和文件"""
    # 定义文件树结构，使用字典表示目录，字符串表示文件
    directory_structure = {
        '.idea': {},  # IDEA 项目配置
        'src': {
            'main': {
                'java': {
                    'com': {
                        'example': {
                            'plugin': {
                                'UI': {},  # 界面相关类
                                'ZhihuPlugin.java': None,  # 插件主类
                                'ZhihuService.java': None,  # 知乎API服务
                                'MdProcessor.java': None,  # Markdown处理器
                            },
                            'action': {
                                'SubmitToZhihuAction.java': None,  # 提交动作
                            }
                        }
                    }
                },
                'resources': {
                    'META-INF': {
                        'plugin.xml': None,  # 插件配置清单
                    },
                    'icons': {
                        'zhihu-icon.svg': None,  # 插件图标
                    },
                    'messages': {
                        'ZhihuBundle.properties': None,  # 国际化资源
                    }
                }
            }
        },
        'build.gradle': None,  # 构建脚本
        'gradle.properties': None,  # gradle配置
        'README.md': None,  # 插件说明文档
    }

    def process_node(path, node):
        """递归处理文件树节点"""
        if isinstance(node, dict):
            # 如果是目录，创建目录并处理子节点
            os.makedirs(path, exist_ok=True)
            for name, child in node.items():
                child_path = os.path.join(path, name)
                process_node(child_path, child)
        elif isinstance(node, str) or node is None:
            # 如果是文件，创建空文件
            if node is None:
                open(path, 'a').close()
            else:
                with open(path, 'w') as f:
                    f.write(node)

    # 从根目录开始处理
    process_node(root_dir, directory_structure)
    print(f"已成功创建目录结构到: {os.path.abspath(root_dir)}")

if __name__ == "__main__":
    # 指定根目录名称
    root_directory = "zhihu-md-plugin"
    create_directory_structure(root_directory)