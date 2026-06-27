# demos

包含若干排序算法的可视化脚本示例。

文件：
- `sort_visuals.py`：一站式排序可视化器，支持下面算法：
  - bubble, insertion, selection, shell, merge, quick3, heap, radix

运行示例：

交互显示（弹出窗口显示动画）：

```bash
python sort_visuals.py --algo bubble --size 50 --maxval 100
```

保存为 mp4（需要已安装 ffmpeg 并在 PATH 中）：

```bash
python sort_visuals.py --algo heap --size 80 --maxval 200 --save heap_demo.mp4
```

参数说明：
- `--algo` 算法名
- `--size` 数组长度
- `--maxval` 随机数组最大值
- `--seed` 随机种子（可重复结果）
- `--interval` 动画帧间隔（毫秒）
- `--save` 指定文件名保存动画（需要 ffmpeg）

注意：GUI 环境下会弹出 matplotlib 窗口；在无图形环境下请用 `--save` 将动画保存为视频（需 ffmpeg）。

建议：若要观察更慢的动画效果，请使用 `--interval 200`（单位 ms）或更大值。生成 GIF 时使用 `--save algo_demo.gif`，示例：

```bash
python sort_visuals.py --algo heap --size 20 --maxval 100 --interval 200 --seed 1 --save heap_demo.gif
```
