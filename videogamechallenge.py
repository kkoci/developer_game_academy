import math

# Point data
points = [
    (28, 42, 1, "North"),
    (27, 46, 2, "East"),
    (16, 22, 3, "South"),
    (40, 50, 4, "West"),
    (8, 6, 5, "North"),
    (6, 19, 6, "East"),
    (28, 5, 7, "South"),
    (39, 36, 8, "West"),
    (12, 34, 9, "North"),
    (36, 20, 10, "East"),
    (22, 47, 11, "South"),
    (33, 19, 12, "West"),
    (41, 18, 13, "North"),
    (41, 34, 14, "East"),
    (14, 29, 15, "South"),
    (6, 49, 16, "West"),
    (46, 50, 17, "North"),
    (17, 40, 18, "East"),
    (28, 26, 19, "South"),
    (2, 12, 20, "West")
]

def VisiblePoints(point_x, point_y, max_distance, direction, angle):
    def is_within_cone(px, py, angle_start, angle_end):
        angle_to_point = math.degrees(math.atan2(py - point_y, px - point_x))
        if angle_to_point < 0:
            angle_to_point += 360
        if angle_start <= angle_end:
            return angle_start <= angle_to_point <= angle_end
        else:
            return angle_to_point >= angle_start or angle_to_point <= angle_end

    direction_angles = {
        "North": 90,
        "East": 0,
        "South": 270,
        "West": 180
    }
    
    direction_angle = direction_angles[direction]
    angle_start = (direction_angle - angle) % 360
    angle_end = (direction_angle + angle) % 360
    
    visible_points = []
    
    for px, py, num, dir in points:
        distance = math.sqrt((px - point_x) ** 2 + (py - point_y) ** 2)
        if distance <= max_distance and is_within_cone(px, py, angle_start, angle_end):
            visible_points.append((px, py, num, dir))
    
    return visible_points

# Example usage:
visible_points = VisiblePoints(1, 45, 20, "East", 45)
print(visible_points)
