#include <windows.h>
#include <stdio.h>


int main() {
    HWND hwnd = GetConsoleWindow(); // 获取窗口句柄，这里以控制台窗口为例
    RECT rect;
    GetClientRect(hwnd, &rect); // 获取客户区域的坐标

    int titleBarHeight = GetSystemMetrics(SM_CYCAPTION); // 获取标题栏的高度

    int titleBarWidth = (rect.right - rect.left); // 客户区域的宽度即为标题栏的宽度

    printf("Title Bar Width: %d\n", titleBarWidth);

    return 0;
}
