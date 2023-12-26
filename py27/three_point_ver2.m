clear all
close all
clc

x = [rand rand rand];
f = x.^4 -12*x.^3 + 47*x.^2 - 75*x + 10;
d = x(min_x) - x(max_x);
anpha = 0.01;
max_x = find(f==max(f));
max_y = find(f==min(f));
temp = x(min_x)+anpha*d;

%axis([min(x)-1,max(x)+1,min(f)-1,max(f)+1]);
%plot(x,f,'red')
for i = 1:5
    
end

