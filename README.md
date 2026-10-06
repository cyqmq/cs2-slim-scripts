# CS2 Slim 一键安装指令生成器

选择环境变量，自动生成 **Linux (`curl | bash`)** 与 **Windows (`irm | iex`)** 一键安装命令的静态网页，部署于 GitHub Pages。

👉 在线使用：<https://cyqmq.github.io/cs2-slim-scripts/>

## 功能

- 可视化选择全部环境变量（`CS2_MODE` / `CS2_MAPS` / `CS2_FEATURES` / `CS2_WORKDIR` / `CS2_PACKAGE` / `CS2_DRY_RUN` / `CS2_GH_PROXY` / `CS2_PANEL`）
- 内置可选地图（de_mirage / de_inferno / de_ancient / …）与可选功能（bots / metamod / metamod-win / css / css-win）
- 功能按平台自动路由：`metamod`、`css` 只进入 Linux 命令，`metamod-win`、`css-win` 只进入 Windows 命令；选择 `css` / `css-win` 自动带上对应平台的 `metamod` / `metamod-win`
- 实时生成 Linux / Windows 一键安装命令，支持一键复制
- 配置自动保存在 URL hash 中，可分享链接给他人直接使用
- 深色终端风格 UI，桌面 / 移动端自适应

## 开发

纯静态单文件，无任何依赖：

```bash
# 本地预览
python -m http.server 8080
# 打开 http://localhost:8080
```

## 数据来源

- 主仓库：<https://github.com/cyqmq/cs2-slim-replica>
- 选配地图：<https://github.com/cyqmq/cs2-slim-maps>
- 选配功能：<https://github.com/cyqmq/cs2-slim-features>