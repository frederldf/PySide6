//
//  Circle.h
//  HelloWorld
//
//  Created by admin on 14/1/12.
//  Copyright (c) 2014年 LDF. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Circle : NSObject
{
    float rx;
    float ry;
    
}
-(id)initWithRadiusX:(float)x andRaduusY:(float)y;
-(float)area;
@end
