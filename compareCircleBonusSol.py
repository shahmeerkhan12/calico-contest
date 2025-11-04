def solve(N: int, X: list[float], Y: list[float]) -> float:
    import math
    
    # Calculate centroid (average of all points)
    avgX = sum(X) / N
    avgY = sum(Y) / N
    
    # Convert 33 degrees to radians
    rad = math.radians(33)
    cos_rad = math.cos(rad)
    sin_rad = math.sin(rad)
    
    # Project points onto rotated axes
    proj_x = []
    proj_y = []
    
    for x, y in zip(X, Y):
        # Center the point
        dx = x - avgX
        dy = y - avgY
        
        # Project onto rotated x-axis (33 degrees)
        proj_on_x = dx * cos_rad + dy * sin_rad
        # Project onto rotated y-axis (33+90=123 degrees)
        proj_on_y = -dx * sin_rad + dy * cos_rad
        
        proj_x.append(proj_on_x)
        proj_y.append(proj_on_y)
    
    # Find width and height in rotated coordinate system
    width = max(proj_x) - min(proj_x)
    height = max(proj_y) - min(proj_y)
    
    # Return area
    return width * height


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx]); idx += 1
    
    for _ in range(T):
        N = int(data[idx]); idx += 1
        X = []
        Y = []
        
        for __ in range(N):
            x = float(data[idx]); idx += 1
            y = float(data[idx]); idx += 1
            X.append(x)
            Y.append(y)
        
        result = solve(N, X, Y)
        print(f"{result:.15f}")


if __name__ == '__main__':
    main()