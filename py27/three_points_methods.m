clear
clc
format long
% Initial bracketing interval.
x = [rand rand rand];

f = x.^4 -12*x.^3 + 47*x.^2 - 75*x + 10;

% Find interpolating polynomial
temp = 0.5*(x(1)-x(2)) + 0.5*((f(1)-f(2)*(f(2)-f(3))*(f(3)-f(1)))/((x(2)-x(3))*f(1)+(x(3)-x(1))*f(2)+(x(1)-x(2))*f(3)));
x = [x(2),x(3),temp];
it = 1;

while abs(x(3)-x(2)) > 10^(-32) && abs(f(3)-x(2)) > 10^(-32)
    f = x.^4 -12*x.^3 + 47*x.^2 - 75*x + 10;
    temp = 0.5*(x(1)-x(2)) + 0.5*((f(1)-f(2)*(f(2)-f(3))*(f(3)-f(1)))/((x(2)-x(3))*f(1)+(x(3)-x(1))*f(2)+(x(1)-x(2))*f(3)));
    x = [x(2),x(3),temp];
    it = it + 1;
%     if it == 5
%         break
%     end
    temp
    pause(1)
end
disp('Estimated Critical Point: ')
disp(f(2))
disp('at the point x = ')
disp(x(2))
disp('Iterations: ')
disp(it)
