% first comment
% second comment

close all;
clear variables;
clc;
format long;

% some data
N = 10000;
M = 80000;
dt = 1e-5
r = zeros(3 * N, M);
v = zeros(3 * N, M);


r(:, 1) = rand(3 * N, 1);
v(:, 1) = rand(3 * N, 1);

a = [1 2 3; 4 5 6; 7 8 8]

for i=2:M
  v(:, i) = v(:, i-1) - dt * r(:, i-1);
  r(:, i) = r(:, i-1) + dt * v(i, :);
end
x = r(1:N, :)
y = r(N+1:2*N, :)
z = r(2*N+1:end, :)


plot_text = text(0.8, 0, ...
                  't = 1.0', ...
                  'units', 'normalized', ...
                  'FontSize', 12, ...
                  'interpreter', 'latex');

figure(1);
plotting = plot3(x(:, 1), y(:, 1), z(:1))
hold('on')
xlabel('blabla')
ylabel('blublu')
zlabel('gragra')
