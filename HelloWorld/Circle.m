//
//  Circle.m
//  HelloWorld
//
//  Created by admin on 14/1/12.
//  Copyright (c) 2014年 LDF. All rights reserved.
//

#import "Circle.h"

@implementation Circle

-(id) init{
    self = [super init];
    return self;
}
-(id)initWithRadiusX:(float)x andRaduusY:(float)y{
    rx=x;
    ry=y;
    return [self init];
}
-(float)area{
    return M_PI*rx*ry;
}
+(void)log:(NSString *)msg{
    NSLog(@"%@",msg);
}

@end
